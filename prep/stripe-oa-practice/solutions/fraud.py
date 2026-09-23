"""Your solution for fraud. See the corresponding file in problems/."""
from fractions import Fraction

def getThreshold(m, merchants, thresholds):
    family = merchants[m]
    return thresholds[family]

def meetsFraudThreshold(fraud_ch, total_ch, threshold):
    # print(f"fr {fraud_ch}, tot: {total_ch}, thres: {threshold}")

    if '.' in threshold:
        return Fraction(fraud_ch , total_ch) >= Fraction(threshold)
    else:
        return fraud_ch >= int(threshold)


def solve(data: dict, part: int = 3) -> list[str]:
    merchants = data["merchants"]
    thresholds = data["thresholds"]
    min_charges = int(data["min_charges"])
    fraud_codes = data["fraud_codes"]
    safe_codes = data["safe_codes"]
    events = data["events"]

    fraud_evs = {} # merc: [fraud_count, totalcharge]
    meets_threshold = []
    seen_ch = set()
    seen_dispute = set()
    ch_accepted = {} #c_id: [merc, code]

    for ev in events:
        ev_split = ev.split(",")
        ev_formatted = [e.strip() for e in ev_split]

        if len(ev_formatted) == 4:
            # Potential Charge Event

            action, ch, merc, code = ev_formatted

            if action != "CHARGE":
                continue

            if merc not in merchants.keys():
                continue

            if code not in fraud_codes and code not in safe_codes:
                continue

            if not ch or ch in seen_ch:
                continue

            seen_ch.add(ch)

            if merc in fraud_evs.keys():
                fraud_evs[merc][1] += 1
                if code in fraud_codes:
                    fraud_evs[merc][0] += 1
                    
            else:
                if code in fraud_codes:
                    fraud_evs[merc] = [1, 1]
                else:
                    fraud_evs[merc] = [0, 1]

            ch_accepted[ch] = [merc, code]            
        
        elif len(ev_formatted) == 2:
            # Potential Dispute event

            action, ch = ev_formatted

            if action != "DISPUTE" or part != 3:
                continue

            if not ch or ch not in seen_ch or ch in seen_dispute:
                continue

            seen_dispute.add(ch)

            if ch not in ch_accepted:
                continue

            d_merc, d_code = ch_accepted[ch]

            if d_code in safe_codes:
                continue

            fraud_evs[d_merc][0] -= 1

             

        else:
            continue

        # print("events: ", fraud_evs.items())

    for m, counts in fraud_evs.items():
        threshold = getThreshold(m, merchants, thresholds)
        if meetsFraudThreshold(counts[0], counts[1], threshold) and counts[1] >= min_charges:
            meets_threshold.append(m)

    return sorted(meets_threshold)

if __name__ == "__main__":
    data = {
        "merchants": {"m1": "retail"},
        "thresholds": {"retail": "2"},
        "min_charges": 1,
        "fraud_codes": ["stolen", "lost"],
        "safe_codes": ["ok"],
        "events": [
            "CHARGE,c1,m1,stolen",
            "CHARGE,c2,m1,ok",
            "CHARGE,c3,m1,stolen",
        ],
    }

    print(solve(data, part=1))