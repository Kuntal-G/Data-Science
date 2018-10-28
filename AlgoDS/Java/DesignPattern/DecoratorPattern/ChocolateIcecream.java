public class ChocolateIcecream extends IcecreamDecorator{

	public ChocolateIcecream(Icecream ice) {
		super(ice);
		// TODO Auto-generated constructor stub
	}
	
	
	@Override
	public void toppings() {
		super.toppings();
		System.out.println("Chocolate added");
		
	}

}
