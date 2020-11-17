open class Animal(var color: String = "") {
  init {
    println("From Animal: $color")
  }
}

class Dog(color: String = "", var breed: String = ""): Animal(color) {
  init {
    println("From Dog: $color and $breed")
  }
}

fun main() {
  val dog = Dog("black", "pug")
  dog.color = "white"
}
