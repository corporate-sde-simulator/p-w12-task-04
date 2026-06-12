# Beginner Explanatory Guide: OPS-402: Fix Broken Alerting Rules

> **Task Type**: Product Task  
> **Domain/Focus**: Python Fundamentals, Alerting Systems

---

## 1. The Goal (In-Depth Beginner Explanation)

### The Core Problem
The alerting system in our application is currently malfunctioning, leading to significant issues in monitoring system performance. Specifically, it is firing critical alerts for minor problems while failing to alert for actual critical issues. This misbehavior can cause unnecessary panic among the operations team and may lead to overlooking genuine problems that require immediate attention. 

The root of the problem lies in the incorrect conditions set for three alert rules within the code. For instance, the CPU alert is set to trigger at a threshold of greater than 9%, which is far too low for a critical alert. Similarly, the memory alert is incorrectly checking the free memory percentage instead of the used memory percentage, which inversely represents the actual memory usage. Lastly, the error rate alert is based on total errors rather than the per-minute error rate, which is essential for timely responses to issues. Fixing these rules is crucial to ensure that the alerting system accurately reflects the system's health, allowing the team to respond appropriately to real problems.

### Jargon Buster (Key Terms Explained)
* **Alerting System**: An alerting system is a mechanism that monitors the performance of applications or systems and notifies users when certain thresholds are crossed. For example, if CPU usage exceeds a certain percentage, the system sends an alert to the operations team to investigate the issue.
  
* **Threshold**: A threshold is a predefined limit that, when crossed, triggers an alert. For instance, if the CPU usage threshold is set at 90%, any usage above this percentage will trigger an alert. This helps in identifying when a system is under stress.

* **Metrics**: Metrics are quantitative measures used to assess the performance of a system. In our context, metrics like CPU usage, memory usage, and error rates provide insights into how well the system is functioning.

* **Operator**: An operator is a symbol that specifies the type of comparison to be made in a condition. Common operators include `>`, `<`, and `>=`. For example, the operator `>` checks if one value is greater than another.

### Expected Outcome
After implementing the necessary fixes, the alerting system should function correctly, triggering alerts only when actual critical thresholds are crossed. 

**Before vs. After Comparison**:
- **Before**: The CPU alert triggers at > 9%, leading to false alarms for minor CPU usage. Memory alerts check free memory instead of used memory, and error rate alerts are based on total errors rather than per-minute rates.
- **After**: The CPU alert triggers at > 90%, accurately reflecting high CPU usage. Memory alerts check used memory percentage, and error rate alerts are based on the number of errors per minute, ensuring timely notifications for real issues.

---

## 2. Related Coding Concepts & Syntax

### Concept 1: Conditional Statements
#### 📘 Theoretical Overview (50%)
Conditional statements are fundamental programming constructs that allow the execution of certain blocks of code based on whether a condition evaluates to true or false. They are essential for decision-making in programming. Without conditional statements, a program would execute the same code regardless of the input or state of the system, which would limit its functionality and responsiveness.

In Python, conditional statements are implemented using `if`, `elif`, and `else`. The `if` statement checks a condition, and if it evaluates to true, the associated block of code runs. If it evaluates to false, the program can check additional conditions using `elif` or execute a default block of code with `else`.

#### 💻 Syntax & Practical Examples (50%)
* **Language Syntax**:
  ```python
  if condition:
      # Code to execute if condition is true
  elif another_condition:
      # Code to execute if another_condition is true
  else:
      # Code to execute if none of the above conditions are true
  ```

* **Real-World Application**:
  ```python
  cpu_usage = 95
  if cpu_usage > 90:
      print("Critical alert: CPU usage is high!")
  elif cpu_usage > 70:
      print("Warning: CPU usage is moderate.")
  else:
      print("CPU usage is normal.")
  ```

### Concept 2: Functions
#### 📘 Theoretical Overview (50%)
Functions are reusable blocks of code that perform a specific task. They help organize code into manageable sections, making it easier to read, maintain, and debug. Functions can take inputs (parameters) and return outputs (return values), allowing for flexibility and reusability across different parts of a program.

In Python, functions are defined using the `def` keyword, followed by the function name and parentheses containing any parameters. The code block within the function is indented, and the function can be called by its name followed by parentheses.

#### 💻 Syntax & Practical Examples (50%)
* **Language Syntax**:
  ```python
  def function_name(parameters):
      # Code to execute
      return value
  ```

* **Real-World Application**:
  ```python
  def check_cpu_usage(cpu_percent):
      if cpu_percent > 90:
          return "Critical alert: CPU usage is high!"
      return "CPU usage is normal."

  alert_message = check_cpu_usage(95)
  print(alert_message)  # Output: Critical alert: CPU usage is high!
  ```

---

## 3. Step-by-Step Logic & Walkthrough

1. **Step 1: Locate and Analyze the Target File**
   * Navigate to the `alertingEngine.py` file within the `p-w12-task-04` folder. This file contains the logic for the alerting rules.
   * Focus on the `create_default_rules` function, specifically the lines where the alert rules are added using the `add_rule` method.

2. **Step 2: Input Verification & Validation**
   * Ensure that the thresholds and metrics used in the alert rules are correct. For example, check that the CPU alert is set to trigger at > 90% and not > 9%. 

3. **Step 3: Core Implementation / Modification**
   * Modify the `create_default_rules` function:
     - Change the CPU alert threshold from 9 to 90.
     - Update the memory alert to check `used_memory_percent` instead of `free_memory_percent`.
     - Adjust the error rate alert to use `errors_per_minute` instead of `total_errors`.

   Here’s how the modified rules should look:
   ```python
   engine.add_rule('High CPU', 'cpu_percent', '>', 90, 'critical')
   engine.add_rule('High Memory', 'used_memory_percent', '>', 80, 'warning')
   engine.add_rule('High Error Rate', 'errors_per_minute', '>', 5, 'critical')
   ```

4. **Step 4: Output Verification & Testing**
   * After making the changes, run the test suite using `pytest` to ensure all tests pass. This will confirm that the alerting rules are functioning as expected and that the system behaves correctly under various conditions.

---

## 4. Detailed Walkthrough of Test Cases

### Test Case 1: Standard / Success Case
* **Description**: This test checks if the alerting system correctly triggers an alert for high CPU usage.
* **Inputs**:
  ```json
  {
      "cpu_percent": 95
  }
  ```
* **Step-by-Step Execution Trace**:
  1. The input value of 95% CPU usage is received by the `check_metrics` function.
  2. The function checks the condition for the 'High CPU' rule, which is set to trigger if CPU usage is greater than 90%.
  3. Since 95% is greater than 90%, the alert is triggered, and an alert dictionary is created.
  4. The function returns the alert indicating that the CPU usage is critical.

* **Expected Output**: 
  ```json
  {
      "rule": "High CPU",
      "value": 95,
      "threshold": 90,
      "severity": "critical"
  }
  ```

### Test Case 2: Edge Case / Validation Fail
* **Description**: This test checks if the alerting system does not trigger an alert for normal CPU usage.
* **Inputs**:
  ```json
  {
      "cpu_percent": 50
  }
  ```
* **Step-by-Step Execution Trace**:
  1. The input value of 50% CPU usage is received by the `check_metrics` function.
  2. The function checks the condition for the 'High CPU' rule, which is set to trigger if CPU usage is greater than 90%.
  3. Since 50% is not greater than 90%, the alert is not triggered, and no alert dictionary is created.
  4. The function returns an empty list, indicating no alerts were fired.

* **Expected Output**: 
  ```json
  []
  ``` 

This detailed guide should provide a comprehensive understanding of the task at hand, the necessary coding concepts, and the steps required to implement the solution effectively.