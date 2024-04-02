import java.io.*;
import java.util.*;

public class Main {
    static HashMap<Long, Long> hm = new HashMap<>();

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int A = Integer.parseInt(st.nextToken());
        int B = Integer.parseInt(st.nextToken());
        int C = Integer.parseInt(st.nextToken());
        System.out.println(getMod(A, B, C));

    }

    static long getMod(long base, long exp, long dividor) {
        if (exp == 1) {
            return base % dividor;
        } else {
            if (hm.containsKey(exp)) return hm.get(exp);
            else {
                long A = exp / 2;
                long B = exp - A;

                long retA = getMod(base, A, dividor);
                long retB = getMod(base, B, dividor);

                long ret = (retA * retB) % dividor;
                hm.put(exp, ret);
                return ret;
            }
        }
    }
}