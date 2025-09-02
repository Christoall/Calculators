//mini java calculator with gui
import javax.swing.*;
import java.awt.*;


public class CalculatorGUI extends JFrame {
    
    private JTextField number1Field, number2Field, resultField;

    public CalculatorGUI() {
        setTitle("Java Calculator");
        setSize(350, 250);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setLayout(new GridLayout(5, 2, 5, 5));

        // Labels and text fields
        add(new JLabel("Number 1:"));
        number1Field = new JTextField();
        add(number1Field);

        add(new JLabel("Number 2:"));
        number2Field = new JTextField();
        add(number2Field);

        add(new JLabel("Result:"));
        resultField = new JTextField();
        resultField.setEditable(false);
        add(resultField);

        // Buttons
        JButton addBtn = new JButton("Add");
        JButton subBtn = new JButton("Subtract");
        JButton mulBtn = new JButton("Multiply");
        JButton divBtn = new JButton("Divide");

        add(addBtn);
        add(subBtn);
        add(mulBtn);
        add(divBtn);

        // Action listeners
        addBtn.addActionListener(e -> calculate("add"));
        subBtn.addActionListener(e -> calculate("subtract"));
        mulBtn.addActionListener(e -> calculate("multiply"));
        divBtn.addActionListener(e -> calculate("divide"));

        setVisible(true);
    }

    // Functions
    private double add(double a, double b) {
        return a + b;
    }

    private double subtract(double a, double b) {
        return a - b;
    }

    private double multiply(double a, double b) {
        return a * b;
    }

    private double divide(double a, double b) {
        if (b == 0) {
            JOptionPane.showMessageDialog(this, "Cannot divide by zero!");
            return 0;
        }
        return a / b;
    }

    // Calculate function
    private void calculate(String operation) {
        try {
            double num1 = Double.parseDouble(number1Field.getText());
            double num2 = Double.parseDouble(number2Field.getText());
            double result = 0;

            switch (operation) {
                case "add":
                    result = add(num1, num2);
                    break;
                case "subtract":
                    result = subtract(num1, num2);
                    break;
                case "multiply":
                    result = multiply(num1, num2);
                    break;
                case "divide":
                    result = divide(num1, num2);
                    break;
            }

            resultField.setText(String.valueOf(result));
        } catch (NumberFormatException e) {
            JOptionPane.showMessageDialog(this, "Please enter valid numbers.");
        }
    }

    public static void main(String[] args) {
        new CalculatorGUI();
    }
}

