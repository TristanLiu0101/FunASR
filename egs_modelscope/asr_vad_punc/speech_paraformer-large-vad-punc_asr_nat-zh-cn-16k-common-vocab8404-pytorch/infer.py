from modelscope.pipelines import pipeline
from modelscope.utils.constant import Tasks

if __name__ == '__main__':
    # audio_in = 'https://isv-data.oss-cn-hangzhou.aliyuncs.com/ics/MaaS/ASR/test_audio/asr_example_zh.wav'
    # audio_in = "C:/Users/liuzhechen/Desktop/S0002/SCP/wav.scp"
    # output_dir = "C:/Users/liuzhechen/Desktop/S0002/outputs_v032"
    audio_in = "C:/Users/liuzhechen/Desktop/asr_test/scp/wav.scp"
    output_dir = "C:/Users/liuzhechen/Desktop/asr_test/outputs_v0.3.3"
    inference_pipeline = pipeline(
        task=Tasks.auto_speech_recognition,
        model='damo/speech_paraformer-large-vad-punc_asr_nat-zh-cn-16k-common-vocab8404-pytorch',
        model_revision="v1.2.1",
        vad_model='damo/speech_fsmn_vad_zh-cn-16k-common-pytorch',
        vad_model_revision="v1.1.8",
        punc_model='damo/punc_ct-transformer_zh-cn-common-vocab272727-pytorch',
        punc_model_revision="v1.1.6",
        ngpu=1,
        output_dir = output_dir,
    )
    rec_result = inference_pipeline(audio_in=audio_in)
    print(rec_result)

