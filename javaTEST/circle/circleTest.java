public class circleTest
{
    public static void main(String[] args)
    {
        Circle c1 = new Circle(3);
        System.out.println(c1.area());
        System.out.println(c1.preimeter());
    }
}


abstract class Shape
{
    public abstract double area();
    public abstract double preimeter();
}

class Circle extends Shape
{
    private double r;

    public Circle(double r)
    {
        this.r = r;
    }
    public double area()
    {
        return 3.14*r*r;
    }
    public double preimeter()
    {
        return 2*3.14*r;
    }
}
