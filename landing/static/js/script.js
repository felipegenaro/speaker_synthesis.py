const selector = selector => document.querySelector(selector);

let recognizing;
let recognition = new window.webkitSpeechRecognition();
recognition.continuous = true;
recognition.lang = 'pt-BR';

recognition.onresult = (event) => {
        for (let i = event.resultIndex; i < event.results.length; ++i) {
                if (event.results[i].isFinal) {
                        textarea.value += event.results[i][0].transcript;
                }
        }
}

const reset = () => {
        recognizing = false;
        selector('#buttonSpeech').innerHTML = "Click para Falar";
}

const toggleStartStop = () => {
        if (recognizing) {
                recognition.stop();
                reset();
        } else {
                recognition.start();
                recognizing = true;
                selector('#buttonSpeech').innerHTML = "Click para Parar";
                textarea.value = "";
        }
}

const listen = () => {
        let hear = new SpeechSynthesisUtterance;

        hear.lang = "pt-BR";
        hear.rate = 1;
        hear.text = textarea.value;

        speechSynthesis.speak(hear);
}

reset();
recognition.onend = reset;