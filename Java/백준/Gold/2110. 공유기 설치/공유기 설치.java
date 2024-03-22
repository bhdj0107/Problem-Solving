import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

class Solution {
    public void solution() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken());  // 집의 개수
        int C = Integer.parseInt(st.nextToken());  // 공유기의 개수

        int[] houses = new int[N];
        for (int i = 0; i < N; i++) {
            houses[i] = Integer.parseInt(br.readLine());
        }

        Arrays.sort(houses);  // 집의 좌표를 오름차순으로 정렬

        // 최소 거리와 최대 거리 설정
        int minGap = 1;
        int maxGap = houses[N-1] - houses[0];  // 가장 먼 집과 가장 가까운 집 사이의 거리

        int result = 0;
        while (minGap <= maxGap) {
            int mid = (minGap + maxGap) / 2;
            int count = 1;  // 설치된 공유기 개수
            int prevHouse = houses[0];  // 첫 집에는 무조건 공유기 설치

            for (int i = 1; i < N; i++) {
                int distance = houses[i] - prevHouse;
                if (distance >= mid) {
                    count++;
                    prevHouse = houses[i];
                }
            }

            if (count >= C) {
                result = mid;
                minGap = mid + 1;
            } else {
                maxGap = mid - 1;
            }
        }

        System.out.println(result);
    }
}


public class Main {
    public static void main(String[] argv) throws IOException {
        Solution sol = new Solution();
        sol.solution();
    }
}