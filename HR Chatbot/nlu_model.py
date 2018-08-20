from rasa_nlu.converters import load_data
from rasa_nlu.config import RasaNLUConfig
from rasa_nlu.model import Trainer
from rasa_nlu.model import Metadata,Interpreter

def train_nlu(data,config,model_dir):
    training_data= load_data(data)
    trainer=Trainer(RasaNLUConfig(config))
    trainer.train(training_data)
    model_directory=trainer.persist(model_dir,fixed_model_name="HRQueryNLU")


def run_nlu():
    interpreter= Interpreter.load('./models/nlu/default/HRQueryNLU',RasaNLUConfig('config_spacy.json'))
    print(interpreter.parse("i cant see my salary slip , i wonder how can i get it"))
    print(interpreter.parse("i will get into car"))

if __name__ == '__main__':
    train_nlu('./data/data.json','./config_spacy.json','./models/nlu')
    run_nlu()
    
