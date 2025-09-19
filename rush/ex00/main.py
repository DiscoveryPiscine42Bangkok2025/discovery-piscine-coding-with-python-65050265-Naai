from checkmate import checkmate

def main():
    
    board = ("...Q..\n"
             ".....B\n"
             "......\n"
             "K.....\n"
             "....R..\n")
    
    checkmate(board)

if __name__ == "__main__":
    main()