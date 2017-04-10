public class Problem_002 {
	public static void main (String[] args) {
		int a = 1;
		int b = 2;
		int total = 0;
		while (b <= 4000000) {
			if (b%2 == 0) {
				total += b;
			}
			b = b + a; 
			a = b - a;
		}
		System.out.println(total);
	}
}
