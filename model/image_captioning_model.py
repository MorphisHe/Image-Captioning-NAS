from torch import nn
from .encoder import EncoderCNN
from .decoder import DecoderRNN


class ConvRNN(nn.Module):
    def __init__(self, encoder_params, decoder_params, vocab_size):
        super(ConvRNN, self).__init__()

        # create encoder, encoder
        self.encoder = EncoderCNN(**encoder_params)
        self.decoder = DecoderRNN(**decoder_params, vocab_size=vocab_size)

    def forward(self, images, captions, lengths):
        img_feats = self.encoder(images)
        outputs = self.decoder(img_feats, captions, lengths)

        return outputs
