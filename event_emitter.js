class EventEmitter {
    constructor() {
        // Initialize a map to store event names and their callbacks
        this.subscriptions = {};
    }

    subscribe(event, callback) {
        // If the event doesn't exist, initialize an empty array for it
        if (!this.subscriptions[event]) {
            this.subscriptions[event] = [];
        }

        // Add the callback to the event's subscription list
        this.subscriptions[event].push(callback);

        // Return an object with an unsubscribe method
        return {
            unsubscribe: () => {
                const index = this.subscriptions[event].indexOf(callback);
                if (index !== -1) {
                    this.subscriptions[event].splice(index, 1);
                }
            }
        };
    }

    emit(event, args = []) {
        // If the event has no subscriptions, return an empty array
        if (!this.subscriptions[event]) {
            return [];
        }

        // Call all the subscribed callbacks with the provided arguments
        return this.subscriptions[event].map(callback => callback(...args));
    }
}

// Example usage:
const emitter = new EventEmitter();

// Subscribe to an event
const sub1 = emitter.subscribe('firstEvent', () => 5);
const sub2 = emitter.subscribe('firstEvent', () => 6);

// Emit the event
console.log(emitter.emit('firstEvent'));  // [5, 6]

// Unsubscribe from the first subscription
sub1.unsubscribe();

// Emit the event again
console.log(emitter.emit('firstEvent'));  // [6]
