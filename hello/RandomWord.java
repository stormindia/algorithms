import edu.princeton.cs.algs4.StdIn;
import edu.princeton.cs.algs4.StdOut;
import edu.princeton.cs.algs4.StdRandom;


public class RandomWord {
    public static void main(String[] args) {
        String currChamp = "";
        int currIndex = 0;
        while (!StdIn.isEmpty()) {
            currIndex++;
            String word = StdIn.readString();
            if (StdRandom.bernoulli(1.0 / currIndex)) {
                currChamp = word;
            }
        }
        StdOut.println(currChamp);
    }
}