/**
 * Builder Pattern in Java
 *  @author Kuntal
 */
public class Employee {
	//Mandatory attribute
	private String name;
	private int age;
	
	// Optional attribute
	private long salary;
	private boolean isEngineer;
	


	public String getName() {
		return name;
	}
	public int getAge() {
		return age;
	}
	public long getSalary() {
		return salary;
	}
	public boolean isEngineer() {
		return isEngineer;
	}
	
	private Employee(EmployeeBuilder builder){
		this.name=builder.name;
		this.age=builder.age;
		this.salary=builder.salary;
		this.isEngineer=builder.isEngineer;
		
	}

	
	private void testHello(){
		System.out.println("Hello Employee Builder");
	}
	
	public static class EmployeeBuilder{
		
		private String name;
		private int age;
		
		// Optional attribute
		private long salary;
		private boolean isEngineer;
		
		
		public EmployeeBuilder(String name, int age){
			this.name=name;
			this.age=age;
		}
		
		public EmployeeBuilder setName(String name){
			this.name=name;
			
			return this;
		}
		
		public EmployeeBuilder setAge(int age){
			this.age=age;
			
			return this;
		}
		
		
		public EmployeeBuilder setSalary(long salary){
			this.salary=salary;
			
			return this;
		}
		
		
		public EmployeeBuilder isEngineer(boolean engineer){
			this.isEngineer=engineer;
			
			return this;
		}
		
		
		
		
		public  Employee build(){
			
			return new Employee(this);
		}


		
		
	}


	public static void main(String[] args) {
		Employee empbuild=new Employee.EmployeeBuilder("Kuntal",30).setSalary(100l).isEngineer(true).build();
		System.out.println(empbuild.getAge());
		empbuild.testHello();
	}
	

}
