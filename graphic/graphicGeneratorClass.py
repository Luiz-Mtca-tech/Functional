conjunto = [[[1, -1], [2, -12], [3, -2], [4, -5], [5, -10], [6, -17]]]

class MathGraphi():
    def generateGraph(self, vector):
        graphic = ""
        x = -40
        y = 20
        run = True
        print("|------------------------------------------------------------|")
        while(run == True):

            #verifica se chegou no final da linha
            if x == 41:
                print("new line")
                
                #verifica se chegou no fim do quadro
                if y > -21:
                    #pula para a proxima linha
                    y -= 1
                    graphic += "|\n|"
                else:
                    #finaliza o quadro
                    print("table finished!")
                    run = False

                x = -40
            #variavel para verificar se o digito já foi inserido na string
            is_ready = False
        
            for item in vector:
                #se a posição for a divisória do plano cartesiano
                if y == 0 or x == 0:
                    if is_ready == False:
                        graphic += "."
                        is_ready = True
                #se a posição for a de um vetor marque o ponto com "0"
                elif x == item[0] and y == item[1]:
                    graphic += "0"
                    x += 1
                    break
                #caso contrario apenas preencha o plano de fundo com "-"
                else:
                    if is_ready == False:
                        graphic += " "
                        is_ready = True


            x += 1 

        print("|--------------------|")
        return graphic