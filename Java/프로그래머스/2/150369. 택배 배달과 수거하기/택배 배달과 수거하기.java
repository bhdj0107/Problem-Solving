import java.util.*;

class Plan {
    public int position;
    public int amount;
    Plan(int position, int amount) {
        this.position = position;
        this.amount = amount;
    }
    
    public String toString() {
        return "(" + this.position + ", " + this.amount + ")";
    }
}

class Schedule {
    public Stack<Plan> deliveriesq = new Stack<>();
    public Stack<Plan> pickupsq = new Stack<>();
    
    Schedule(int[] deliveries, int[] pickups, int n) {
        for (int i = 0; i < n; i++) {
            Plan p;
            if (deliveries[i] > 0) {
                p = new Plan(i + 1, deliveries[i]);
                deliveriesq.add(p);
            }
            
            if (pickups[i] > 0) {
                p = new Plan(i + 1, pickups[i]);
                pickupsq.add(p);
            }
        }
    }
    
    public void print() {
        for (int i = deliveriesq.size() - 1; i >= 0; i--) {
            System.out.println(deliveriesq.get(i));
        }
        System.out.println("------------");
        for (int i = pickupsq.size() - 1; i >= 0; i--) {
            System.out.println(pickupsq.get(i));
        }
    }
    
    public int simulationAndgetDistance(int cap) {
        int ret = getLastPos() * 2;
        int rCap;
        
        // 배달 시뮬레이션
        rCap = cap;
        while (true) {
            if (!isRemainDelivery()) break;
            Plan lastPlan = deliveriesq.pop();
            if (lastPlan.amount > rCap) {
                lastPlan.amount -= rCap;
                rCap = 0;
                deliveriesq.add(lastPlan);
                break;
            } else {
                rCap -= lastPlan.amount;
            }
        }
  
        rCap = cap;
        // 픽업 시뮬레이션
        while (true) {
            if (!isRemainPickup()) break;
            Plan lastPlan = pickupsq.pop();
            if (lastPlan.amount > rCap) {
                lastPlan.amount -= rCap;
                rCap = 0;
                pickupsq.add(lastPlan);
                break;
            } else {
                rCap -= lastPlan.amount;
            }
        }
        
        return ret;
    }
    
    public int getLastPos() {
        int d, p;
        if (!deliveriesq.empty()) d = deliveriesq.get(deliveriesq.size() - 1).position;
        else d = 0;
        
        if (!pickupsq.empty()) p = pickupsq.get(pickupsq.size() - 1).position;
        else p = 0;
        return Integer.max(d, p);
    }
    
    public Boolean isRemainDelivery() {
        return !deliveriesq.empty();
    }
    
    public Boolean isRemainPickup() {
        return !pickupsq.empty();
    }
}

class Solution {
    public long solution(int cap, int n, int[] deliveries, int[] pickups) {
        long answer = 0;
        Schedule schedule = new Schedule(deliveries, pickups, n);
        while (true) {
            if (!schedule.isRemainDelivery() && !schedule.isRemainPickup()) break;
            answer += schedule.simulationAndgetDistance(cap);
        }
        return answer;
    }
}