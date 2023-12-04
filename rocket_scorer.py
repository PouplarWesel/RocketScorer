class RocketScorer:
    def __init__(self):
        self.duration_goal_range = (43, 46)
        self.altitude_performance_goal = 820

    def get_rocket_specs(self):
        weight = float(input("Enter the rocket weight at liftoff (grams): "))
        length = float(input("Enter the rocket length (millimeters): "))
        upper_diameter = float(input("Enter the upper body tube diameter (inches): "))
        lower_diameter = float(input("Enter the lower body tube diameter (inches): "))
        altitude = float(input("Enter the rocket altitude (feet): "))
        duration = float(input("Enter the rocket duration (seconds): "))
        return weight, length, upper_diameter, lower_diameter, altitude, duration

    def calculate_duration_score(self, duration):
        if self.duration_goal_range[0] <= duration <= self.duration_goal_range[1]:
            return 0
        else:
            below_range_penalty = abs(self.duration_goal_range[0] - duration) * 4
            above_range_penalty = abs(duration - self.duration_goal_range[1]) * 4
            return min(below_range_penalty, above_range_penalty)

    def calculate_altitude_score(self, altitude):
        return abs(self.altitude_performance_goal - altitude)

    def calculate_total_score(self, duration, altitude):
        duration_score = self.calculate_duration_score(duration)
        altitude_score = self.calculate_altitude_score(altitude)
        return duration_score + altitude_score

    def run_scorer(self):
        print("Enter rocket specifications:")
        weight, length, upper_diameter, lower_diameter, altitude, duration = self.get_rocket_specs()

        score = self.calculate_total_score(duration, altitude)

        print(f"\nRocket Score: {score}")


if __name__ == "__main__":
    scorer = RocketScorer()
    scorer.run_scorer()
