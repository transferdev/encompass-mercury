import cryptocur

class Currency(cryptocur.CryptoCur):
    p2pkh_version = 66
    p2sh_version = 85
    genesis_hash = '9672529bc958a440a8acd061d914120d44c914a06454b82d3e1cd68fe4f1f916'

    coin_name = 'Transfercoin'
    code = 'TX'

    irc_nick_prefix = 'E_'
    irc_channel = '#cryptomist'
