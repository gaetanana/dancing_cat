import random
import time
import os
cat_frames_inspired_high_disco = [
    """
                             \  ∧＿∧
                              \( ^ω^)
                               \    \\
                               └─┬┬─┘\\
                                 ||   \\
                               ┌┘  └┐ 
                               |    |                    
                               U    U 
    """,
    """
                                ∧＿∧  /
                               (^ω^ )/
                               /    /
                              /└─┬┬─┘
                             /   ||
                               ┌┘  └┐ 
                               |    |                   
                               U    U 
    """,
    """
                                ∧＿∧     ̲
                               ( •ω•)   │ 
                           ┌───|    |───┘
                          ̲│   └─┬┬─┘
                                 ||
                               ┌┘  └┐ 
                               |    |                   
                               U    U 
    """,
    """
                          ̲     ∧＿∧
                           │   (•ω• )     
                           └───|    |───┐
                               └─┬┬─┘   │̲
                                 ||      
                               ┌┘  └┐ 
                               |    |                    
                               U    U 
    """,
    """
                                  ∧＿∧
                                 ( 'ω') 
                                 /    /
                                /└─┬┬─┘
                               / / ||
                              / /┌┘  └┐ 
                                 /    /                   
                                U   U 
    """,
    """
                                  ∧＿∧
                                 ('ω' ) 
                                 \    \\ 
                                 └─┬┬─┘\\
                                   || \ \\
                                 ┌┘  └┐\ 
                                 \    \                    
                                  U   U 
    """,
    """
                                 ∧＿∧  \\
                                (•ω• )/
                                \    \\
                            \  /└─┬┬─┘
                             \/   ||
                                ┌┘  └┐ 
                                |    |                   
                                U    U 
    """,
    """
                             ∧＿∧
                            (•ω• )
                          ┌─|    |─┐
                          \ └─┬┬─┘ /
                           \  ||  /
                            ┌┘  └┐ 
                            |    |                    
                            U    U 
    """,
    """
                               / ∧＿∧  
                               \( •ω•)
                                \    \\  /
                                └─┬┬─┘\\/
                                  ||
                                ┌┘  └┐ 
                                |    |                   
                                U    U 
    """,
    """      
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