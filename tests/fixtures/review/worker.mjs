export default {
  async fetch(request, env) {
    const actor = await env.AUTH.verify(request.headers.get('Authorization'));
    if (!actor) return new Response('unauthorized', { status: 401 });
    const { customerId, note } = await request.json();
    console.log(JSON.stringify({ headers: [...request.headers], body: { customerId, note } }));
    await env.DB.prepare(`UPDATE customers SET note = '${note}' WHERE id = '${customerId}'`).run();
    return Response.json({ ok: true });
  }
};
