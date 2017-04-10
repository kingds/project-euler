import java.lang.Math;

class Problem_003 {

    public static void main(String[] args) {
        long n = 600851475143L;
        int i = (int) Math.sqrt(n);
        if (i % 2 == 0) {
            i++;
        }
        for (int a = i; a > 3; a -= 2) {
            if (n % a == 0 && isPrime(a)) {
                System.out.println(a);
                break;
            }
        }
    }

    public static boolean isPrime(int n) {
        if (n % 2 == 0 || n == 0) {
            return false;
        }
        for (int i = 3; i < Math.sqrt(n); i += 2) {
            if (n % i == 0) {
                return false;
            }
        }
        return true;
    }

}