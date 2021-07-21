int find_missing(const vector<int>& input) {
  // calculate sum of all elements
  // in input vector
  auto sum_of_elements = std::accumulate(
    input.begin(), input.end(), 0);
  // There is exactly 1 number missing
  int n = input.size() + 1;
  int actual_sum = (n * ( n + 1 ) ) / 2;
  return actual_sum - sum_of_elements;
}

void test(int n) {
  int missing_element = rand() % n + 1;
  vector<int> v;
  for (int i = 1; i <= n; ++i) {
    if (i == missing_element) {
      continue;
    }
    v.push_back(i);
  }
  int actual_missing = find_missing(v);
  cout << "Expected Missing = " << missing_element << " Actual Missing = " << actual_missing << endl;
}

int main() {
  srand (time(NULL));
  for (int i = 1; i < 10; ++i)
    test(100000);

  return 0;
}