open class Animal {
  var color: String = ""
  constructor(color: String) {
    this.color = color
    println("From Animal: $color")
  }
}

class Dog: Animal {
  var breed: String = ""
  constructor(color: String, breed: String): super(color) {
    this.breed = breed
    println("From Dog: $color and $breed")
  }
}

fun main() {
  val dog = Dog("black", "pug")
  dog.color = "white"
}
