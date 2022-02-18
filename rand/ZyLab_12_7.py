"""Anthony Tran
PSID: 1957342
ZyLab 12.7"""


def get_age():
    age_input = int(input())
    if 18 <= age_input <= 75:
        return age_input
    raise ValueError("Invalid age.")


def fat_burning_heart_rate(var1):
    heart_rate = (220 - var1) * 0.7
    return heart_rate


if __name__ == "__main__":
    try:
        age = get_age()
        print("Fat burning heart rate for a", age, "year-old:", fat_burning_heart_rate(age), "bpm")
    except ValueError as var:
        print(var)
        print("Could not calculate heart rate info.\n")
