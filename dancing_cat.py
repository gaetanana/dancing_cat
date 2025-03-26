import random
import time
import os
cat_frames_inspired_high_disco = [
    r"""
                             \  ∧＿∧
                              \( ^ω^)
                               \    \
                               └─┬┬─┘\
                                 ||   \
                               ┌┘  └┐ 
                               |    |                    
                               U    U 
    """,
    r"""
                                ∧＿∧  /
                               (^ω^ )/
                               /    /
                              /└─┬┬─┘
                             /   ||
                               ┌┘  └┐ 
                               |    |                   
                               U    U 
    """,
    r"""
                                ∧＿∧     ̲
                               ( •ω•)   │ 
                           ┌───|    |───┘
                          ̲│   └─┬┬─┘
                                 ||
                               ┌┘  └┐ 
                               |    |                   
                               U    U 
    """,
    r"""
                          ̲      ∧＿∧
                           │   (•ω• )     
                           └───|    |───┐
                               └─┬┬─┘   │̲
                                 ||      
                               ┌┘  └┐ 
                               |    |                    
                               U    U 
    """,
    r"""
                                  ∧＿∧
                                 ( 'ω') 
                                 /    /
                                /└─┬┬─┘
                               / / ||
                              / /┌┘  └┐ 
                                 /    /                   
                                U   U 
    """,
    r"""
                                  ∧＿∧
                                 ('ω' ) 
                                 \    \ 
                                 └─┬┬─┘\
                                   || \ \
                                 ┌┘  └┐\ 
                                 \    \                    
                                  U   U 
    """,
    r"""
                                 ∧＿∧  \
                                (•ω• )/
                                \    \
                            \  /└─┬┬─┘
                             \/   ||
                                ┌┘  └┐ 
                                |    |                   
                                U    U 
    """,
    r"""
                             ∧＿∧
                            (•ω• )
                          ┌─|    |─┐
                          \ └─┬┬─┘ /
                           \  ||  /
                            ┌┘  └┐ 
                            |    |                    
                            U    U 
    """,
    r"""
                               / ∧＿∧  
                               \( •ω•)
                                \    \  /
                                └─┬┬─┘\/
                                  ||
                                ┌┘  └┐ 
                                |    |                   
                                U    U 
    """,
    r"""      
                          \   ∧＿∧   /
                           \ (^ω^ ) /
                            └|    |┘ 
                             └─┬┬─┘  
                               ||   
                             ┌┘  └┐ 
                             |    |                    
                             U    U 
    """]
def dance_single_cat(num_frames):
    for _ in range(num_frames):
        for frame in cat_frames_inspired_high_disco:
            os.system('cls' if os.name == 'nt' else 'clear')
            print(frame)
            time.sleep(0.5)

def main():
    print(dance_single_cat(10))
  
if __name__ == "__main__":
    main()