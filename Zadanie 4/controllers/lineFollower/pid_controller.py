class PIDController:
    def __init__(self, kp, ki, kd, setpoint, min_output, max_output):
        self.kp = kp
        self.ki = ki
        self.kd = kd
        self.setpoint = setpoint
        self.min_output = min_output
        self.max_output = max_output

        self.error_sum = 0
        self.last_error = 0

    def update(self, measured_value):
        error = self.setpoint - measured_value
        self.error_sum += error
        d_error = error - self.last_error
        self.last_error = error
        if self.error_sum >= 1:
            self.error_sum = 1

        output = self.kp * error+ self.ki*self.error_sum + self.kd * d_error
        output = max(self.min_output, min(self.max_output, output))
        return output