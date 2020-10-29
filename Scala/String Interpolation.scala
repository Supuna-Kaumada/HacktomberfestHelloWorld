class StringExample{  
    var pi = 3.14  
    def show(){  
        println(s"value of pi = $pi")  
    }  
}  
  
object MainObject{  
    def main(args:Array[String]){  
        var s = new StringExample()  
        s.show()  
    }  
}  