public class IcecreamDecorator implements Icecream{
	
	protected Icecream icecream;
	
	public IcecreamDecorator(Icecream ice){
		this.icecream=ice;
	}

	@Override
	public void toppings() {
		this.icecream.toppings();
		
	}

}
