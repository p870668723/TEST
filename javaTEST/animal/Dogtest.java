class Animal
{
    private String name;
    private int id;
    public Animal(String name, int id)
    {
        this.name = name;
        this.id = id;
        System.out.println("in Animal construction function");
    }
    public void run()
    {
        System.out.println("Animal can run");
    }
    public void voice()
    {
        System.out.println("Animal has voice");
    }
    public String get_name()
    {
        return name;
    }
    public void set_name(String name)
    {
        this.name = name;
    }

    public int get_id()
    {
        return id;
    }

    public void set_id(int id)
    {
        this.id=id;
    }
}

class Dog extends Animal
{
    private String type;
    public Dog(String name, int id, String type)
    {
        super(name, id);
        this.type = type;
        System.out.println("in Dog construction function");
    }
    public void run()
    {
        System.out.println("Dog run fast");
    }
    public void voice()
    {
        System.out.println("Dog  wang wang wang");
    }
    public void diplay()
    {
        System.out.println("name: "+get_name());
        System.out.println("id: "+get_id());
        System.out.println("type: "+get_type());
    }
    public String get_type()
    {
        return this.type;
    }
    public void set_type(String type)
    {
        this.type = type;
    }
}

public class Dogtest
{
    public static void main(String[] args)
    {
        System.out.println(args[0]);
        Dog dog1 = new Dog("hg",232,"tugou");
        dog1.voice();
        dog1.run();
        dog1.diplay();
    }
}
