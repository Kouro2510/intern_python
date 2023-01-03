public class Main {
    String action;
    int speed;
  // Static method
  static void Animal(boolean checkAnimal) {
    if(checkAnimal==true){
        System.out.println("This is Lion");
    }
    else{
        System.out.println("This is Bird");
    }
  }

  // Public method
  public void Run(String checkAction,int checkSpeed) {
       action = checkAction;
       speed=checkSpeed;
        if(action == "run"){
            System.out.print("is Running "+speed+" km/h");
        }
        else{
             System.out.println("is Slepping");
        }
  }

  // Main method
  public static void main(String[] args) {

    Main myObj = new Main(); // Create an object of Main
    myObj.Animal(false); // Call the public method on the object
    myObj.Run("run",500);
  }
}