package heap;

public class Tester {


    public static void main(String[] args){
        heap test1=new heap(1,10);
        test1.insert(3);
        test1.insert(1);
        test1.insert(10);
        test1.insert(9);
        test1.insert(6);
        test1.insert(12);
        test1.insert(2);
        System.out.println("Before pop:");
        test1.print();
        System.out.println(test1.popMax());
        System.out.println("After pop:");
        test1.print();
    }
}
