import time

def track_progress(total_steps):
    for step in range(total_steps):
        print(f'Progress: {step + 1}/{total_steps}')
        time.sleep(1)  # Simulate time taken for each step

# Example usage
track_progress(10)
