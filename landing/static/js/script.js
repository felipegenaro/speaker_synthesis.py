const selector = selector => document.querySelector(selector);

let recognizing;
let recognition = new window.webkitSpeechRecognition();
recognition.continuous = true;
recognition.lang = "en-CA";

let uploadFile = "";
let documentReader = new FileReader();

let rate = selector("#rate");
let rateValue = selector("#rateValue");

let pitch = selector("#pitch");
let pitchValue = selector("#pitchValue");

let speaker = "";

let listenRate = 1;
let listenPitch = 1;
let listenLang = "en-CA";

if(selector("#buttonUploadTextFile")) updateFile = selector("#buttonUploadTextFile");
if(selector("#speaker")) speaker = selector("#speaker");

recognition.onresult = (event) => {
        for (let i = event.resultIndex; i < event.results.length; ++i) {
                if (event.results[i].isFinal) {
                        selector("#textarea-stt").value += event.results[i][0].transcript;
                }
        }
}

const reset = () => {
        recognizing = false;
        selector("#buttonSpeech").innerHTML = "Say";
}

const toggleStartStop = () => {
        if (recognizing) {
                recognition.stop();
                
                if(selector("#buttonSpeech")) reset();
        } else {
                recognition.start();
                recognizing = true;
                selector("#buttonSpeech").innerHTML = "Stop";
                selector("#textarea-stt").value = "";
        }
}

const listen = (txtAreaName) => {
        let hear = new SpeechSynthesisUtterance;

        hear.lang = listenLang;
        hear.rate = listenRate;
        hear.pitch = listenPitch;
        hear.text = selector(`#${txtAreaName}`).value;

        speechSynthesis.speak(hear);
}

uploadFile.onchange = () => {
        let file = selector("#buttonUploadTextFile").files[0];
        
        documentReader.readAsText(file);        

        let txtArea = selector("#textarea-tts");
        txtArea.value = "Waiting until your file is loadded...";
}

documentReader.onload = (e) => {
        let txtArea = selector("#textarea-tts");

        try {
                txtArea.value = e.target.result;
        } catch(e) {
                alert("Somethin went Wrong!" + e.message);
        } 
};

rate.onchange = () => {
        rateValue.innerHTML = `Speed ${rate.value}`;
        listenRate = rate.value;
}

pitch.onchange = () => {
        pitchValue.innerHTML = `Pitch ${pitch.value}`;
        listenPitch = pitch.value;
}

speaker.onchange = () => {
        listenLang = speaker.value;
}


if(selector("#buttonSpeech")) reset();
recognition.onend = reset;