public class test{
    public static void change(int[] v){
        v[0]=10;
    }
    public static void main(String[] args) {
        System.out.println("begin");
        int[] value = {1,2,3,4};
        change(value);
        System.out.println(value[0]);
    }
}
