# CryptoQuiz

CryptoQuiz is a cutting-edge mobile application designed to transform the quiz gaming experience by integrating blockchain technology. Our project brings a unique twist to the traditional quiz genre, focusing on blockchain-related questions and leveraging Ethereum and Celo for in-game transactions and rewards.

## Features

- **Blockchain Integration**: Utilizes Ethereum and Celo for secure in-game transactions and rewards.
- **Blockchain-Related Questions**: Focuses on educating users about blockchain technology through quiz questions.
- **Secure Sign-Up**: Users are encouraged to input their private keys, which are not stored on the server.
- **React Native Frontend**: A smooth and responsive mobile application.
- **Django Backend**: Robust backend support using Django.
- **Smart Contracts**: Written using Remix for managing transactions and rewards.

## Tech Stack

- **Backend**: Django
- **Frontend**: React Native
- **Blockchain**: Ethereum, Celo
- **Smart Contracts**: Solidity, developed using Remix

## Installation

### Backend (Django)

1. Clone the repository:
    ```bash
    git clone https://github.com/your-repo/cryptoquiz.git
    cd cryptoquiz
    ```

2. Create and activate a virtual environment:
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Apply migrations:
    ```bash
    python manage.py migrate
    ```

5. Run the server:
    ```bash
    python manage.py runserver
    ```

### Frontend (React Native)

1. Navigate to the `frontend` directory:
    ```bash
    cd frontend
    ```

2. Install dependencies:
    ```bash
    npm install
    ```

3. Run the application:
    ```bash
    npx react-native run-android  # For Android
    npx react-native run-ios      # For iOS
    ```

### Smart Contracts

1. Open [Remix IDE](https://remix.ethereum.org/).
2. Load the smart contract files located in the `contracts` directory.
3. Compile and deploy the contracts on the Ethereum and Celo networks.


## Smart Contract (DumbQuesScore)

The `DumbQuesScore` smart contract is an integral part of CryptoQuiz, facilitating secure management of game scores and reward distributions on the blockchain. Developed in Solidity and deployed on Ethereum and Celo networks, this contract ensures transparency and reliability in handling in-game transactions and rewards.

### Functionalities

1. **Game Score Recording**:
   - `saveGameScores`: Allows the owner to record game scores for different teams. Each game is associated with a unique game ID and stores the team name and score.

2. **Reward Distribution**:
   - `distributeReward`: Enables the owner to distribute rewards in Theta tokens to specific teams based on their performance in the quizzes. Rewards are transferred securely to the team's address upon distribution.

3. **Game Information Retrieval**:
   - `getGameDetails`: Provides access to detailed information about a specific game identified by its game ID, including the team name, score, and whether it has been recorded.

4. **Batch Game Details Retrieval**:
   - `getAllGameDetails`: Retrieves all recorded game details, including team names, scores, and recording statuses, across all games recorded so far.

### Usage

- **Integration**: Integrate this smart contract into CryptoQuiz's backend to ensure seamless recording and reward distribution based on quiz performance.
- **Ownership**: Only the contract owner can record game scores and distribute rewards, ensuring control over the reward mechanism.
- **Blockchain Security**: Leveraging Ethereum and Celo, transactions are secure and transparent, fostering trust among players.

### Deployment

## Usage

1. **Sign Up**: Users sign up by inputting their private key. Note that the private key is not stored on the server.
2. **Wallet Requirement**: Users must have an Ethereum or Celo wallet to make in-game purchases.
3. **Play Quizzes**: Participate in quizzes focused on blockchain technology.
4. **Earn Rewards**: Earn Ether or Celo as rewards for completing quizzes.

## Contributing

We welcome contributions! Please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Commit your changes (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Open a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Thanks to the open-source community for providing valuable tools and frameworks.
- Special thanks to the blockchain enthusiasts who helped shape this project.

