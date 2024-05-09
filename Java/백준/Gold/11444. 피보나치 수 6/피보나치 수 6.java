import java.io.*;
import java.util.*;

public class Main {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    static HashMap<Long,Long> hm = new HashMap<>();

    public static void main(String[] args) throws IOException {
        Long N = Long.parseLong(br.readLine());
        System.out.println(fibo(N));
    }

    static Long fibo(Long n) {
        if (n == 0L) return 0L;
        else if (n == 1L) return 1L;
        else if (n == 2L) return 1L;
        else if (hm.containsKey(n)) return hm.get(n);

        Long half = n / 2 + 1;
        Long divider = 1000000007L;

        Long a = fibo(half) % divider * fibo(n + 1 - half) % divider;
        Long b = fibo(half - 1) % divider * fibo(n - half) % divider;
        Long c = (a + b) % divider;
        hm.put(n, c);
        return c;
    }
}