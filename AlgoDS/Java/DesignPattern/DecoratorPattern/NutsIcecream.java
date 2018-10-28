public class NutsIcecream extends IcecreamDecorator{

	public NutsIcecream(Icecream ice) {
		super(ice);
		
		
	}

	
	
	@Override
	public void toppings() {
		super.toppings();
		System.out.println("Nuts added");
		
	}
	
}
