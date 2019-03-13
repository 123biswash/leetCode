import java.util.*;


class User {
    private String name;
    private int id;

    public User(String name, int id) {
        this.name = name;
        this.id = id;
    }
    public int getId(){
        return id;
    }
    public String getName(){
        return name;
    }
    public void setName(String name){
        this.name= name;
    }
    @Override
    public String toString() {
        return name + " " + id;
    }
    
    // Overriding the compareTo method
    public int compareTo(User u) {
        if(u.getId()<this.getId()){
            return 1;
        }else{
            return -1;
        }
    }
    @Override
    public boolean equals(Object o) {
        if (o == this) {
            return true;
        }
        if (!(o instanceof User)) {
            return false;
        }
        User u = (User) o;
        return this.getId()==u.getId();
    }
}

class SortbyId implements Comparator<User> {
    // Used for sorting in ascending order of
    public int compare(User a, User b) {
        return a.compareTo(b);
    }
}

class UserService {
    public String userServiceName;
    public UserService registeredService= null;

    // public HashSet<UserService> registeredServices;
    public ArrayList<User> userList = new ArrayList<User>();
    @Override
    public String toString() {
        return userServiceName;
    }
    public UserService(String serviceName) {
      userServiceName=serviceName;
    }
    public void addUser(User user) {
        if(registeredService!=null){
            registeredService.addHelper(user);
        }
        this.addHelper(user);
    }
    public void addHelper(User user){
        if (!userList.contains(user)) {
            userList.add(user);
        } else {
            int i = userList.indexOf(user);
            userList.get(i).setName(user.getName());
        }
        Collections.sort(userList, new SortbyId());
    }
    public void deleteUser(User user) {
        if (registeredService != null) {
            registeredService.deleteHelper(user);
        }
        this.deleteHelper(user);
    }

    public void deleteHelper(User user){
        int i = userList.indexOf(user);
        userList.remove(i);

    }
    public List<User> getUsers() { 
      return userList; 
    }

    public void registerListener(UserService userService) {
        this.registeredService=userService;
    }

    public void deregisterListener(UserService userService) {
        this.registeredService=null;
    }
}
