import java.applet.*;
import java.awt.Button;
import java.awt.Color;

public class AddButton extends Applet{
    Button button;
    public void init(){
        setBackground(Color.lightGray);
        button=new Button("I am Button!");
        add(button);
    }
}