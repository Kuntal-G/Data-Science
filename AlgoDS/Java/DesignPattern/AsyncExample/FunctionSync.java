import java.util.function.Function;

public class FunctionSync implements Function<String,String>{

	@Override
	public String apply(String name) {
	
		return "hello"+name;
	}

}
