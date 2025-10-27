#include <bits/stdc++.h>
#include <windows.h>
using namespace std;

int main() {
    srand(time(0));
    deque<string> words = {"apple", "banana", "grape", "mango", "cherry", "orange", "peach", "melon", "kiwi", "plum"};
    random_shuffle(words.begin(), words.end());
    deque<string> showWords;
    for (int i = 0; i < 5; i++) showWords.push_back(words[i]);
    cout << "MEMORY GAME \n";
    cout << "Memorize these words:\n";
    for (auto &w : showWords) cout << w << " ";
    cout << "\n";
    Sleep(5000);
    system("cls");
    cout << "Now type the words you remember (in any order):\n";
    deque<string> userWords;
    for (int i = 0; i < 5; i++) {
        string x;
        cout << "Word " << i + 1 << ": ";
        cin >> x;
        userWords.push_back(x);
    }
    int score = 0;
    for (auto &uw : userWords)
        if (find(showWords.begin(), showWords.end(), uw) != showWords.end()) score++;
    cout << "\nYou remembered " << score << " out of 5 words correctly!\n";
    cout << "Original words were: ";
    for (auto &w : showWords) cout << w << " ";
    cout << "\n";
    if (score == 5) cout << "Excellent memory\n";
    else if (score >= 3) cout << "Good job\n";
    else cout << "Try again! \n";
    return 0;
}
