directories = {
    '/opt/dehydrated': {
        'mode': '0755',
    },
    '/etc/letsencrypt': {
        'mode': '0755',
    },
}

git_deploy = {
    '/opt/dehydrated': {
        'needs': [
            'directory:/opt/dehydrated'
        ],
        'repo': 'https://github.com/lukas2511/dehydrated.git',
        'rev': 'master',
    },
}
