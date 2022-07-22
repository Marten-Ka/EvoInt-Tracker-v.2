<script lang="ts">
	export let title: string;
	export let content: string = '';
	export let right_side: boolean = false;

	let className: string;
	export { className as class };
</script>

<div
	class={`container xl:w-[90%] flex gap-12 flex-col xl:flex-row ${
		right_side && 'flex-col xl:flex-row-reverse text-center'
	} justify-between items-center text-center ${className}`}
>
	<div class={`w-full lg:w-1/2 max-w-2xl flex flex-col ${right_side && 'text-center'} gap-2`}>
		<p class="text-2xl sm:text-3xl md:text-4xl lg:text-5xl mb-4 font-bold uppercase text-gray-100">{title}</p>
		{#if content}
			<p class="text-gray-400 text-base sm:text-lg md:text-xl lg:text-2xl text-center lg:text-justify">{content}</p>
		{:else}
			<slot name="content" />
		{/if}
		<slot name="left_slot" />
	</div>
	<div class="w-full lg:w-1/2">
		<slot name="right_slot" />
	</div>
</div>

<style lang="postcss">
	.container {
	}
</style>
