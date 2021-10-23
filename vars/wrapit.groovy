def call(Closure body) {
  echo "Hello from library"
  body()
  echo "Goodbye from library"
}
