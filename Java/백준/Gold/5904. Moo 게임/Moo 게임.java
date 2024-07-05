import java.io.*;
import java.util.*;

public class Main {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    public static void main(String[] args) throws IOException {
        // S_k(27) -> 1073741792
        int N = Integer.parseInt(br.readLine()) - 1;
        int length = 1073741792;
        int k = 27;
        
        while (true) {
            int subLen = (length - (k + 3)) / 2;
            // check N is in center
            if (subLen <= N && N < length - subLen) {
                N -= subLen;
                if (N != 0) bw.write("o\n");
                else bw.write("m\n");
                break;
            } else {
                if (!(N < subLen)) N -= (subLen) + (k + 3);
                length = subLen;
                k -= 1;
            }
        }
        bw.flush();
        bw.close();
    }
}