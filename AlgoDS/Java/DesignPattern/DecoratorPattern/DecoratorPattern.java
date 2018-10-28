public class DecoratorPattern {
	
	
	
	public static void main(String[] args) {
		
		Icecream choco=new ChocolateIcecream(new NutsIcecream(new Plain()));
		choco.toppings();
		
	}
	


}
