

const options = {
	authProvider,
};

const client = Client.init(options);

const chatMessage = {body: {content: 'Hello world'}};

await client.api('/teams/00025a58-c957-44e3-b8bf-f65d71d2f72d/channels/19:dbf6bd07f4cd41bbbc1a60b6d9f1bd81@thread.tacv2/messages')
	.post(chatMessage);