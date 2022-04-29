import string

def toggle_text(text: str) -> str:
    t_list = []
    
    for n in text:
        
        if ord("a") <= ord(n) <= ord("z"):
            t_list.append(chr(ord(n) - 32))
            
        elif ord("A") <= ord(n) <= ord("Z"):
            t_list.append(chr(ord(n) + 32))
            
    return "".join(t_list)

def main():
    text = input("영어 소문자를 입력하세요.")
    
    print(toggle_text(text))
    
if __name__ == "__main__":
    main()