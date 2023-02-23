# HTTPS and HTTP imports[#](#https-and-http-imports)

[Stability: 1](documentation.html#stability-index) - Experimental

Importing network based modules using `https:` and `http:` is supported under the `--experimental-network-imports` flag. This allows web browser-like imports to work in Node.js with a few differences due to application stability and security concerns that are different when running in a privileged environment instead of a browser sandbox.

## Imports are limited to HTTP/1[#](#imports-are-limited-to-http1)

Automatic protocol negotiation for HTTP/2 and HTTP/3 is not yet supported.

## HTTP is limited to loopback addresses[#](#http-is-limited-to-loopback-addresses)

`http:` is vulnerable to man-in-the-middle attacks and is not allowed to be used for addresses outside of the IPv4 address `127.0.0.0/8` (`127.0.0.1` to `127.255.255.255`) and the IPv6 address `::1`. Support for `http:` is intended to be used for local development.

## Authentication is never sent to the destination server.[#](#authentication-is-never-sent-to-the-destination-server)

`Authorization`, `Cookie`, and `Proxy-Authorization` headers are not sent to the server. Avoid including user info in parts of imported URLs. A security model for safely using these on the server is being worked on.

## CORS is never checked on the destination server[#](#cors-is-never-checked-on-the-destination-server)

CORS is designed to allow a server to limit the consumers of an API to a specific set of hosts. This is not supported as it does not make sense for a server-based implementation.

## Cannot load non-network dependencies[#](#cannot-load-non-network-dependencies)

These modules cannot access other modules that are not over `http:` or `https:`. To still access local modules while avoiding the security concern, pass in references to the local dependencies:

```mjs
// file.mjs
import worker_threads from "node:worker_threads";
import { configure, resize } from "https://example.com/imagelib.mjs";
configure({ worker_threads });

// https://example.com/imagelib.mjs
let worker_threads;
export function configure(opts) {
  worker_threads = opts.worker_threads;
}
export function resize(img, size) {
  // Perform resizing in worker_thread to avoid main thread blocking
}
```

## Network-based loading is not enabled by default[#](#network-based-loading-is-not-enabled-by-default)

For now, the `--experimental-network-imports` flag is required to enable loading resources over `http:` or `https:`. In the future, a different mechanism will be used to enforce this. Opt-in is required to prevent transitive dependencies inadvertently using potentially mutable state that could affect reliability of Node.js applications.
