import java.io.*;
import java.lang.Math;
class Solution {
    public long solution(int r1, int r2) {
        long answer = 0;
        for (long i = 1; i < r2; i++) {
            int M = (int)Math.floor(Math.sqrt((long)r2 * (long)r2 - i * i));
            double m;
            if (i < r1) {
                m = Math.sqrt((long)r1 * (long)r1 - i * i);
            } else {
                m = 0;
            }
            answer += M - Math.floor(m);
            if ((m - Math.floor(m)) == 0) answer += 1;
        }
        return (answer + 1) * 4;
    }
}